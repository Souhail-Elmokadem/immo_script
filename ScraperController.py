from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from manager_scraper import run_scraper, scraper_classes, scraper_status, threads
from threading import Thread
from database.db_manager import get_connection
from fastapi.responses import JSONResponse
from utils.villes import ville_id_nom
from collections import defaultdict
from apscheduler.schedulers.background import BackgroundScheduler

from database.db_manager import create_database_if_not_exists, create_immobilier_table
from config import DB_CONFIG
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ En prod, restreindre à ton domaine React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def start_all_scrapers_job():
    print("🕓 [Scheduler] Démarrage automatique des scrapers...")
    for name in scraper_classes.keys():
        if name in threads and threads[name].is_alive():
            continue  # already running
        t = Thread(target=run_scraper, args=(name,))
        threads[name] = t
        t.start()

# ⏱️ Planifier toutes les 24h
scheduler = BackgroundScheduler()
scheduler.add_job(start_all_scrapers_job, 'interval',hours=10)  
scheduler.start()

@app.post("/start/{name}")
def start_scraper(name: str):
    if name not in scraper_classes:
        raise HTTPException(status_code=404, detail="Scraper inconnu")

    if name in threads and threads[name].is_alive():
        return {"message": f"{name} est déjà en cours."}

    t = Thread(target=run_scraper, args=(name,))
    threads[name] = t
    t.start()
    return {"message": f"{name} lancé ✅"}

@app.post("/start-all")
def start_all_sequential():
    create_database_if_not_exists(DB_CONFIG["database"])
    create_immobilier_table()
    launched = []
    skipped = []

    for name in scraper_classes.keys():
        if name in threads and threads[name].is_alive():
            skipped.append(name)
            continue

        # Exécution directe sans thread (bloquant)
        scraper_status[name] = "⏳ En cours..."
        try:
            run_scraper(name)
            scraper_status[name] = "✅ Terminé"
            launched.append(name)
        except Exception as e:
            scraper_status[name] = f"❌ Échec: {str(e)}"

    return {
        "launched": launched,
        "skipped": skipped,
        "message": f"{len(launched)} scrapers exécutés séquentiellement, {len(skipped)} ignorés car déjà en cours."
    }


@app.get("/status")
def get_status():
    # S'assurer que tous les scrapers sont présents dans le dict, même s'ils n'ont jamais été lancés
    full_status = {}
    for name in scraper_classes:
        full_status[name] = scraper_status.get(name, "Inactif")

    return JSONResponse(content=full_status)





from fastapi.responses import JSONResponse
from collections import defaultdict

@app.get("/stats")
def get_scraper_stats():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # 🔢 Total annonces
        cursor.execute("SELECT COUNT(*) FROM immobilier")
        total_annonces = cursor.fetchone()[0]

        # 📍 Normaliser villes
        cursor.execute("SELECT ville FROM immobilier")
        rows = cursor.fetchall()
        ville_counts = defaultdict(int)
        for (adresse,) in rows:
            adresse = adresse.lower() if adresse else ""
            matched = False
            for nom_ville in ville_id_nom.values():
                if nom_ville.lower() in adresse:
                    ville_counts[nom_ville] += 1
                    matched = True
                    break
            if not matched:
                ville_counts["Inconnue"] += 1

        ville_stats = [{"ville": k, "count": v} for k, v in ville_counts.items()]
        total_villes = len(ville_counts)

        # 🌐 Par source
        cursor.execute("SELECT source, COUNT(*) as count FROM immobilier GROUP BY source")
        source_stats = [{"source": row[0], "count": row[1]} for row in cursor.fetchall()]
        total_sources = len(source_stats)

        cursor.close()
        conn.close()

        return JSONResponse(content={
            "total_annonces": total_annonces,
            "total_villes": total_villes,
            "total_sources": total_sources,
            "by_ville": sorted(ville_stats, key=lambda x: x["count"], reverse=True),
            "by_source": source_stats
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération des statistiques : {e}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération des statistiques : {e}")

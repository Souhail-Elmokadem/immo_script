import React, { useEffect, useState } from 'react';

export default function Scrape() {
  const [scraperStatus, setScraperStatus] = useState({});
  const [loading, setLoading] = useState(false);
  const [logs, setLogs] = useState([]);

  // Récupérer le statut des scrapers toutes les 3 sec
  useEffect(() => {
    const fetchStatus = () => {
      fetch('http://localhost:8000/status')
        .then(res => res.json())
        .then(data => setScraperStatus(data))
        .catch(err => console.error("❌ Statut erreur :", err));
    };

    fetchStatus(); // initial
    const interval = setInterval(fetchStatus, 3000);
    return () => clearInterval(interval);
  }, []);

  // Démarrer un scraper
  const handleStartScraper = (name) => {
    setLoading(true);
    fetch(`http://localhost:8000/start/${name}`, { method: 'POST' })
      .then(res => res.json())
      .then((data) => {
        addLog(`✅ ${name} démarré`);
        setLoading(false);
      })
      .catch(err => {
        console.error("Erreur start:", err);
        addLog(`❌ Erreur démarrage ${name}`);
        setLoading(false);
      });
  };

  // Démarrer tous les scrapers
  const handleStartAll = () => {
    setLoading(true);
    fetch('http://localhost:8000/start-all', { method: 'POST' })
      .then(res => res.json())
      .then((data) => {
        addLog(`🚀 Tous les scrapers lancés (${data.launched.length})`);
        setLoading(false);
      })
      .catch(err => {
        console.error("Erreur start-all:", err);
        addLog("❌ Erreur de démarrage global");
        setLoading(false);
      });
  };

  // Ajouter un log
  const addLog = (msg) => {
    setLogs(prev => [msg, ...prev.slice(0, 100)]); // max 100 logs
  };

  return (
    <div className="container mt-4">
      <h4 className="mb-3">🧪 Gestion des Scrapers</h4>

      <div className="mb-3">
        <button
          onClick={handleStartAll}
          className="btn btn-primary"
          disabled={loading}
        >
          🚀 Démarrer tous les scrapers
        </button>
      </div>

      <table className="table table-bordered table-striped">
        <thead className="table-light">
          <tr>
            <th>Nom</th>
            <th>Statut</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(scraperStatus).map(([name, status]) => (
            <tr key={name}>
              <td>{name}</td>
              <td>{status}</td>
              <td>
                <button
                  className="btn btn-sm btn-outline-secondary"
                  onClick={() => handleStartScraper(name)}
                  disabled={status.includes("⏳") || loading}
                >
                  🔁 Lancer
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <h6 className="mt-4">📋 Logs</h6>
      <div className="bg-dark text-white p-3 rounded" style={{ maxHeight: '200px', overflowY: 'scroll' }}>
        {logs.length === 0 ? (
          <div className="text-muted">Aucun log pour le moment.</div>
        ) : (
          logs.map((log, index) => <div key={index}>{log}</div>)
        )}
      </div>
    </div>
  );
}

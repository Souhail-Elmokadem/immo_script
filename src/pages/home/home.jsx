import React from 'react'
import DoughnutChart from '../../componants/doughnutChart/doughnutChart';
import BarChart from '../../componants/barChart/barChart';
import BarChartHori from '../../componants/barChartHori/barChartHori';
import CardStats from '../../componants/cardStats/cardStats';

function Home() {

    return (
        <>
            <main className="page-content">
                <div className="row row-cols-1 row-cols-lg-2 row-cols-xl-2 row-cols-xxl-4">
                    <CardStats title="total annonces" suffix=""  />
                    <CardStats title="nombres sites" suffix="sites"  />
                    <CardStats title="nombres villes" suffix="villes"  />
                    
                    <div className="col">
                        <div className="card overflow-hidden rounded-4">
                            <div className="card-body p-2">
                                <div className="d-flex align-items-stretch justify-content-between rounded-4 overflow-hidden bg-primary">
                                    <div className="w-50 p-3 bg-light-primary">
                                        <p className="text-white">Customers</p>
                                        <h4 className="text-white">25.8K</h4>
                                    </div>
                                    <div className="w-50 p-3">
                                        <p className="mb-3 text-white text-end">+ 8.2% <i className="bi bi-arrow-up"></i></p>
                                        <div id="chart4"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="row row-cols-1 row-cols-lg-2">

                    <div className="d-flex justify-content-center">

                        <BarChart />

                    </div>
                    <div className="d-flex justify-content-center">

                        <DoughnutChart />

                    </div>



                </div>

                <div className="row">
                    <BarChartHori />
                    
                </div>








            </main>
        </>
    )
}

export default Home
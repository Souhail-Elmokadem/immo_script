import { Doughnut } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend
} from 'chart.js';
import useFetch from '../../hooks/useFetch/useFetch';
import { useEffect, useState } from 'react';

ChartJS.register(ArcElement, Tooltip, Legend);

const options = {
  cutout: '77%',
  plugins: {
    legend: {
      position: 'bottom',
      labels: {
        boxWidth: 8,
      },
    },
    tooltip: {
      enabled: true,
    },
  },
  maintainAspectRatio: false,
};

export default function DoughnutChart() {
  const [loading, data, error] = useFetch('http://localhost:8000/stats');
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    if (data && data.by_source) {
      const labels = data.by_source.map(v => v.source);
      const values = data.by_source.map(v => v.count);

      setChartData({
        labels,
        datasets: [
          {
            label: 'Biens par site',
            data: values,
            backgroundColor: [
              '#8ea8fd', '#3461ff', '#c1cfff',
              '#fdcb6e', '#e17055', '#00cec9',
              '#6c5ce7', '#fab1a0', '#55efc4',
              '#ffeaa7', '#ff7675', '#fd79a8'
            ],
            borderWidth: 1,
          },
        ],
      });
    }
  }, [data]);

  if (loading) return <div className="text-center">⏳ Chargement...</div>;
  if (error) return <div className="alert alert-danger">❌ Erreur : {error.message}</div>;
  if (!chartData) return <div className="alert alert-warning">Aucune donnée trouvée</div>;

  return (
    <div className="col d-flex">
      <div className="card radius-10 w-100 overflow-hidden">
        <div className="card-body">
          <div className="d-flex align-items-center">
            <h6 className="mb-0">Biens par site</h6>
          </div>
        </div>
        <div style={{ width: '100%', height: '400px' }}>
          <Doughnut data={chartData} options={options} />
        </div>
      </div>
    </div>
  );
}

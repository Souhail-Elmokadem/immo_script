// src/components/charts/LineChart.jsx
import { Line } from 'react-chartjs-2';
import useFetch from '../../hooks/useFetch/useFetch';
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Tooltip,
  Legend,
} from 'chart.js';
import { useEffect, useState } from 'react';

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement, Tooltip, Legend);

const options = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: 'top',
    },
    tooltip: {
      enabled: true,
    },
  },
  scales: {
    y: {
      beginAtZero: true,
    },
  },
};

export default function LineChart() {
  const [loading, data, error] = useFetch('http://localhost:8000/stats');
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    if (data && data.by_source) {
      const labels = data.by_source.map(d => d.source);
      const values = data.by_source.map(d => d.count);

      setChartData({
        labels,
        datasets: [
          {
            label: 'Annonces par site',
            data: values,
            fill: false,
            borderColor: '#3461ff',
            backgroundColor: '#3461ff',
            tension: 0.4, // curved lines
            pointRadius: 5,
            pointHoverRadius: 7,
          },
        ],
      });
    }
  }, [data]);

  if (loading) return <div className="text-center">⏳ Chargement...</div>;
  if (error) return <div className="alert alert-danger">❌ Erreur : {error.message}</div>;
  if (!chartData) return <div className="alert alert-warning">Aucune donnée trouvée</div>;

  return (
    <div className="card radius-10 w-100">
      <div className="card-body">
        <h6 className="mb-3">Annonces par site (Ligne)</h6>
        <div
          className="d-flex justify-content-center align-items-center"
          style={{ width: '100%', height: '400px' }}
        >
          <Line data={chartData} options={options} />
        </div>
      </div>
    </div>
  );
}

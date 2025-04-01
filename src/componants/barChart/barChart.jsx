import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend
} from 'chart.js';
import useFetch from '../../hooks/useFetch/useFetch';
import { useState, useEffect } from 'react';

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

const options = {
  plugins: {
    legend: { position: 'bottom' },
    tooltip: { enabled: true },
  },
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: { beginAtZero: true },
  },
};

export default function BarChart() {
  const [loading, data, error] = useFetch('http://localhost:8000/stats');
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    if (data && data.by_ville) {
      const labels = data.by_ville.map(item => item.ville);
      const values = data.by_ville.map(item => item.count);

      setChartData({
        labels,
        datasets: [
          {
            label: ['Annonces par ville'],
            data: values,
            backgroundColor: '#3461ff',
            borderRadius: 8,
          },
        ],
      });
    }
  }, [data]);

  if (loading) return <div className="spinner-border text-primary" role="status"><span className="visually-hidden">Loading...</span></div>;
  if (error) return <div className="alert alert-danger" role="alert">Error: {error.message}</div>;
  if (!chartData) return <div className="alert alert-warning" role="alert">No data available</div>;

  return (
    <div className="col d-flex">
      <div className="card radius-10 w-100 overflow-hidden">
        <div className="card-body">
          <div className="d-flex align-items-center">
            <h6 className="mb-0">Annonces par ville</h6>
          </div>
        </div>
        <div className="d-flex justify-content-center align-items-center" style={{ width: '100%', height: '400px' }}>
          <Bar data={chartData} options={options} />
        </div>
      </div>
    </div>
  );
}

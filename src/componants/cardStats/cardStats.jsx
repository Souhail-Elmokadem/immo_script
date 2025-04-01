import React, { useEffect, useState } from 'react'
import useFetch from '../../hooks/useFetch/useFetch'

export default function CardStats({title,suffix}) {
    
const [loading, data, error] = useFetch('http://localhost:8000/stats');
const [number,setNumber] = useState(0)

useEffect(() => {
    
    if (data) {
      switch (title) {
        case "total annonces":
            setNumber(data.total_annonces)
            break;
        case "nombres sites":
           setNumber(data.total_sources)
           break;
        case "nombres villes":
           setNumber(data.total_villes)
           break;
        
        default:
            break;
      }
     
    }
  }, [data, title]);
  
  return (
                <div className="col">
                <div className="card overflow-hidden rounded-4">
                    <div className="card-body p-2">
                        <div className="d-flex align-items-stretch justify-content-between  rounded-4 overflow-hidden bg-primary">
                            <div className="w-50 p-3">
                                <p className="text-white">{title}</p>
                                <h4 className="text-white">{number} {suffix}</h4>
                            </div>
                            <div className="w-50 p-3">
                                <p className="mb-3 text-white text-end">+ 16% <i className="bi bi-arrow-up"></i></p>
                                {/* <div id="chart1"></div> */}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
  )
}

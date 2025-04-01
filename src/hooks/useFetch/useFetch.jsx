import React, { useEffect, useState } from 'react'

export default function useFetch(url) {

    const [loading, setLoading] = useState(true);
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);

    const fetchData = async () =>{
        setLoading(true);
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const result = await response.json();
            setData(result);
        } catch (error) {
            setError(error);
        } finally {
            setLoading(false);
        }
    }
    useEffect(() => {
        fetchData();
    }, [url]);

  return [loading, data, error]
}

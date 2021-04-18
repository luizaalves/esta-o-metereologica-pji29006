import React, {useEffect, useState} from 'react';
import api from '../../services/api';
import {Link} from 'react-router-dom';
import './index.css'

export default function Sensores(){
    const [sensores, setSensores] = useState([]);

    useEffect(() => {
        function carregarSensores(){
            api.get('/sensores').then((response=>setSensores(response.data)));
        }
        carregarSensores();
    },[])

    return ( 
        <>
            <h4><strong>Lista de sensores:</strong></h4>
                <ul className="listar-sensores">
                    {sensores.map(sensor => (
                        <li key={sensor.id_sensor}>
                            <Link to={`/editar/${sensor.id_sensor}`} >
                            <button className="btn" type="submit"><strong><div>Nome:{sensor.description}</div><div>ID: {sensor.id_sensor}</div></strong></button>
                            </Link>
                        </li>
                    ))}
                </ul>
        </>
    )
}
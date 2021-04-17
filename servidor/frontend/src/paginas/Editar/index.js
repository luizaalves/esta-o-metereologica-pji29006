import React, {useEffect, useState} from 'react';
import api from '../../services/api';
import {useParams,useHistory} from "react-router-dom";

export default function Editar(){
    const [val_max, value_max] = useState([]);
    const [val_min, value_min] = useState([]);
    // Captura o id do sensor que estará na url
    const { id } = useParams();
    let history = useHistory();

    useEffect(() => {

        async function carregarSensor(){
            var res = await api.get('/sensor',{
                headers: { 'id_sensor':id }
            });
            value_max(res.data.value_max);
            value_min(res.data.value_min);
            
        }
        carregarSensor();
    },[])

    function handleClick(){
        history.push('/sensores');
    }
    
     async function handleSubmit(){
        const data = {
            'value_min': val_min,
            'value_max': val_max
        }
        api.put('/limiares', data, {
            headers: { 'id_sensor':id }
        }).then(history.push('/sensores'));
        
        
        
    }


    return ( 
        <>
            <div><label>{`ID_SENSOR : ${id}`}</label></div>
            <div><label htmlFor="value_min">{'Valor mínimo :'}</label>
            <input
                id="value_min"
                placeholder={val_min}
                value={val_min}
                onChange={event=>value_min(event.target.value)}
            /></div>
            
            <div><label>{'\nValor máximo :'}</label>
            <input
                id="value_max"
                placeholder={val_max}
                value={val_max}
                onChange={event=>value_max(event.target.value)}
            /></div>
            <button onClick={handleSubmit} type='submit' className='btn'>Atualizar limiares</button>
        </>
    )
}

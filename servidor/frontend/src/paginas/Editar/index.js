import React, {useEffect, useState} from 'react';
import api from '../../services/api';
import {useParams,useHistory} from "react-router-dom";

import {toast} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';


export default function Editar(){
    const [val_max, value_max] = useState([]);
    const [val_min, value_min] = useState([]);
    //Armazenar respoosta da leitura de um sensor específico
    var respostaLeitura;
// é possivel customizar a notificação
const CustomToast = () => {
    return (
        <>
        Leitura do Sensor concluída:

        <li>
            <strong>{respostaLeitura.data.type_grandeza}</strong>  
        </li>
        <li>
            <strong>{respostaLeitura.data.value} [{respostaLeitura.data.unit}]</strong>                       
        </li>
        
        </>
    )
}


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

    const notify = () => {
        toast.info(<CustomToast/>, {position: toast.POSITION.TOP_CENTER})
     }

    async function carregarMedida(){
        //usar o await aqui pode dar problema
        respostaLeitura = await api.get('/medidas',{
                headers: { 'id_sensor':id }
          });
            //Pegar valores do sensor exemplo
                //"type_grandeza": "pressure",
                //"value": 1014.18,
                //"unit": "hectopascal"
            
         //notificar Leitura do sensor
         notify()
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

            <button onClick={carregarMedida} className='btn'>Ler Sensor</button>

        </>
    )
}

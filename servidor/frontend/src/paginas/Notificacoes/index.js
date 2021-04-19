import React, {useEffect, useState} from 'react';
import api from '../../services/api';
import {Link} from 'react-router-dom';

import {toast} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import './index.css';

// é possivel customizar a notificação
const CustomToast = () => {
    return (
        <>
        Algo deu errado
        <button onClick={window.location.reload()} className='btn'>clique no botão para recarregar a página</button>
        
        </>
    )
}

toast.configure()

export default function Notificacoes(){

    const [notificacoes, setNotificacoes] = useState([]);

    
       async function carregarNotificacoes(){
           //usar o await aqui pode dar problema
             api.get('/notificacoes').then((response=>setNotificacoes(response.data)));
            
            //notificar que deu tudo certo
            notifySucces()
        }

    
    const notifySucces = () => {
        //Exemplo de como chamar peronalizado
        //toast.warn(<CustomToast/>, {position: toast.POSITION.TOP_CENTER,autoClose: 8000})

        toast.success('Notificações Atualizadas ', {
            position: toast.POSITION.TOP_CENTER,
            autoClose: 3000
        })
    }
    const notifyInfo = () => {
       // toast.info('Status das Notificações', {position: toast.POSITION.TOP_RIGHT})
       toast.info('Sem notificações no momento, clique em "Carregar Notificações" para consultar o sistema ', {position: toast.POSITION.TOP_CENTER})
    }
    const notifyError = () => {
        //toast.error('Erro ao exibir Notificações', {position: toast.POSITION.BOTTOM_RIGHT})
        toast.error('Erro ao exibir Notificações', {
            position: toast.POSITION.TOP_CENTER,
            autoClose: false
        })
    }

    // Informar para carregar a página, criar uma função que identifica quando a lista de notificacoes esta vazia
    if (notificacoes.length === 0){
        console.log("Tamanho da lista de notificacoes é " + notificacoes.length)
        notifyInfo();
    }

    return ( 
        <>
            <h4><strong>Página de notificacoes dos sensores:</strong></h4>

            <button onClick={carregarNotificacoes} className='btn'>Carregar Notificações</button>

            <ul className="listar-notificacoes">
                    {notificacoes.map(notificacao => (
                        <li key={notificacao.id_notify}>
                            <header><strong>O sensor {notificacao.id_sensor}</strong></header>
                            <strong>---------------------------------------------------------------------------</strong>
                            Ultrapassou o limiar de {notificacao.type_grandeza} com valor {notificacao.value} da unidade de medida [{notificacao.unit}] 
                            <body>Horário {notificacao.hora}</body>
                        </li>
                    

                    ))}
            </ul>

        </>
    )
}
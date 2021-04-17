import React from 'react';
import {Link} from 'react-router-dom';

export default function Capa(){

    return (
        <>
            <p>
                Pressione o botão para exibir a <strong>Lista de sensores </strong> da estação.
            </p>
            <Link to="/sensores">
            <button className="btn" type="submit">Listar</button>
            </Link>

            <Link to="/notificacoes">
            <button className="btn" type="submit">Notificações</button>
            </Link>
        </>
    )

}
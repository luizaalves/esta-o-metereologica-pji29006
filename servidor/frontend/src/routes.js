//Necessário importar o React para trabalhar com jsx
import React from 'react';
// Importanto componentes do React
import { BrowserRouter, Switch, Route } from 'react-router-dom';
// Rota dos sensores
import Sensores from './paginas/Sensores';
import Capa from './paginas/Capa';
import Editar from './paginas/Editar';
import Notificacoes from './paginas/Notificacoes';

// Exportar um novo componente

// Comportamento padrão de rotas no React é permitir que mais
// de uma rota seja chamada ao mesmo tempo.
// o Swicth faz com que se limite a uma rota por vez

export default function Rotas(){
    return(
        <BrowserRouter >
            <Switch>
                <Route path="/" exact component={Capa}/>
                <Route path="/sensores" exact component={Sensores}/>
                <Route path="/editar/:id" exact component={Editar}/>
                <Route path="/notificacoes" exact component={Notificacoes}/>
            </Switch>
        </BrowserRouter>
    );
}

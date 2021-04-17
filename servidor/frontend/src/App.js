import logo from './logo.svg';
import './App.css';

//Teste de notificações
//import ReactNotification from 'react-notifications-component'

//Importando arquivos de rotas
import Routes from './routes';
import { BrowserRouter } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
    <div className="App">
    <header className="App-header">
     
      <div className="content">
      <noscript><img src={logo} className="App-logo" alt="logo" /></noscript>
        <Routes />
      </div>

    </header>
  </div></BrowserRouter>
  );
}

export default App;

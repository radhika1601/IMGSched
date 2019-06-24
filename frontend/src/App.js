
import React, { Component } from 'react';
import './App.css';

import GoogleLogin from 'react-google-login';

class App extends Component {

  render() {


    const responseGoogle = (response) => {
      console.log(response);
    }

    return (
      <div className="App">
      <h1>LOGIN WITH GOOGLE</h1>

      <GoogleLogin
        clientId = "570137200285-ac0q9krf77pe1hjgherjif8i3ula5tdn.apps.googleusercontent.com" 
        buttonText="LOGIN WITH GOOGLE"
        onSuccess={responseGoogle}
        onFailure={responseGoogle}
      />

      </div>
    );
  }
}

export default App;
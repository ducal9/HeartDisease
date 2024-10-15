import React, { Component } from 'react';

export class NavBar extends Component {
  render() {
    return (
      <nav className='navbar bg-primary-subtle'>
        <div className='container-fluid'>
          <a className='navbar-brand' href='#'>
            Prediction Heart Disiease App
          </a>
        </div>
      </nav>
    );
  }
}

export default NavBar;

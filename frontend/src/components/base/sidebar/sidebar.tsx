import React from 'react';

const sidebar = [
  {
    chat: {
      label: 'Chat'
    },
    menus: {
      label: 'Menus',
      items:[
      {name: 'Menu 1', href: '#'},
      {name: 'Menu 2', href: '#'},
      {name: 'Menu 3', href: '#'},
    ]},
    account: {
      label: 'Account',
      loginOption: 'Log in'
    }
  }
]

const Sidebar = () => {
  return (
    <div>
      <div>
        MVC Logo
      </div>
      <div>

      </div>
      <div>
        <label></label>
        <ul>
          <li></li>
        </ul>
      </div>
      <div>

      </div>
    </div>
  );
};

export default Sidebar;

import React from 'react';

import styles from './sidebar.module.css';

export const sidebar = {
  action: {
    label: 'Actions',
    chat: { name: 'Chat', href: '#' },
  },
  menuLinks: {
    label: 'Menu Links',
    items: [
      { name: 'Menu 1', href: '#' },
      { name: 'Menu 2', href: '#' },
      { name: 'Menu 3', href: '#' },
    ],
  },
  account: {
    label: 'Account',
    loginOption: { name: 'Log in', href: '#' },
  },
};

const Sidebar = () => {
  return (
    <div className={styles.container}>
      <div>
        <div className={styles.logo}>MVC Logo</div>
        <section>
          <ul>
            <a href={sidebar.action.chat.href}>
              <li>{sidebar.action.chat.name}</li>
            </a>
          </ul>
        </section>
        <section>
          <label>{sidebar.menuLinks.label}</label>
          <ul>
            {sidebar.menuLinks.items.map((item, i) => (
              <a key={i} href={item.href}>
                <li> {item.name}</li>
              </a>
            ))}
          </ul>
        </section>
      </div>
      <section>
        <label>{sidebar.account.label}</label>
        <ul>
          <a href={sidebar.account.loginOption.href}>
            <li>{sidebar.account.loginOption.name}</li>
          </a>
        </ul>
      </section>
    </div>
  );
};

export default Sidebar;

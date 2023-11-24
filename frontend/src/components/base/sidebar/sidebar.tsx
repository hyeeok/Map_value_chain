'use client';

import { useAtomValue } from 'jotai';
import React from 'react';

import { showSidebarAtom } from '@/lib/atoms/base';

import styles from './sidebar.module.css';

export const sidebarData = {
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
      { name: 'Menu 3', href: '#' },
      { name: 'Menu 3', href: '#' },
      { name: 'Menu 3', href: '#' },
      { name: 'Menu 3', href: '#' },
      { name: 'Menu 3', href: '#' },
      { name: 'Menu 3', href: '#' },
      { name: 'Menu 3', href: '#' },
      { name: 'Menu 3', href: '#' },
      { name: 'Menu 3', href: '#' },
      { name: 'Menu 3', href: '#' },
      { name: 'Menu 3', href: '#' },
    ],
  },
  account: {
    label: 'Account',
    loginOption: { name: 'Log in', href: '#' },
  },
};

const Sidebar = () => {
  const showSidebar = useAtomValue(showSidebarAtom);
  console.log(showSidebar);

  return (
    <nav className={`${styles.container} ${!showSidebar && styles.hidden}`}>
      <div className={styles.logo}>MVC Logo</div>
      <section>
        <ul>
          <a href={sidebarData.action.chat.href}>
            <li>{sidebarData.action.chat.name}</li>
          </a>
        </ul>
      </section>
      <label>{sidebarData.menuLinks.label}</label>
      <section className={styles.menulinks}>
        <ul>
          {sidebarData.menuLinks.items.map((item, i) => (
            <a key={i} href={item.href}>
              <li> {item.name}</li>
            </a>
          ))}
        </ul>
      </section>
      <label>{sidebarData.account.label}</label>
      <section>
        <ul>
          <a href={sidebarData.account.loginOption.href}>
            <li>{sidebarData.account.loginOption.name}</li>
          </a>
        </ul>
      </section>
    </nav>
  );
};

export default Sidebar;

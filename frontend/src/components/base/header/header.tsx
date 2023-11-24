'use client';

import { useAtom } from 'jotai';
import { BellIcon, HelpCircle, MenuIcon } from 'lucide-react';
import React from 'react';

import { showSidebarAtom } from '@/lib/atoms/base';

import styles from './header.module.css';

const Header = () => {
  const [showSidebar, setShowSidebar] = useAtom(showSidebarAtom);
  const toggleShowSidebar = () => {
    setShowSidebar(!showSidebar);
  };

  return (
    <header className={styles.container}>
      <div>
        <button onClick={toggleShowSidebar}>
          <MenuIcon size={16} />
        </button>
      </div>
      <div className={styles.title}>Menu name</div>
      <div className={styles.options}>
        <button>
          <BellIcon size={16} />
        </button>
        <button>
          <HelpCircle size={16} />
        </button>
        <div className={styles.language}>
          <select defaultValue="en">
            <option value="en">English</option>
            <option value="kr">한국어</option>
          </select>
        </div>
      </div>
    </header>
  );
};

export default Header;

'use client';

import { useAtom } from 'jotai';
import { BellIcon, HelpCircle, MenuIcon } from 'lucide-react';
import React from 'react';

import { Button } from '@/components/ui/button';
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
        <Button variant="outline" size="icon" onClick={toggleShowSidebar}>
          <MenuIcon className="h-4 w-4" />
        </Button>
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

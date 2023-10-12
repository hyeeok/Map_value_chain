import { BellIcon, HelpCircle, MenuIcon } from 'lucide-react';
import React from 'react';

import styles from './header.module.css';

const Header = () => {
  return (
    <header className={styles.container}>
      <div>
        <button>
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
          <select>
            <option value="en" selected>
              English
            </option>
            <option value="kr">한국어</option>
          </select>
        </div>
      </div>
    </header>
  );
};

export default Header;

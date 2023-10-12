import React from 'react';

import styles from './footer.module.css';

const footerData = {
  company: '(주)그레타',
  address: '서울시 서대문구 신촌로 141 은하빌딩 302호',
  tel: '대표번호',
  support: '고객문의',
  termsOfUse: '서비스 이용약관',
  privacyPolicy: '개인정보 처리 방침',
};

const Footer = () => {
  return (
    <footer className={styles.container}>
      <div>
        <a>
          <span className={styles.company}>{footerData.company}</span>
        </a>
        <p>
          {footerData.address} | {footerData.tel} 070-8548-1024 |
          {footerData.support} support@***.com
        </p>
      </div>
      <div>
        <a className={styles.info}>{footerData.termsOfUse}</a> |{' '}
        <a className={styles.info}>{footerData.privacyPolicy}</a>
      </div>
      <div>Copyright. GRETA Inc. All rights reserved.</div>
    </footer>
  );
};

export default Footer;

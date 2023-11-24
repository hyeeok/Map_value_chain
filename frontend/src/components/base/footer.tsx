import Link from 'next/link';
import React from 'react';

const FooterLink = ({
  href = '#',
  children,
}: {
  href: string;
  children: React.ReactNode;
}) => {
  return (
    <Link href={href} className="hover:underline underline-offset-4">
      {children}
    </Link>
  );
};

const Footer = () => {
  return (
    <footer className="border-t py-6">
      <div className="container flex flex-col items-start text-xs">
        <div
          className="
          flex items-end align-end gap-4
          text-left text-xs leading-6 text-muted-foreground
          "
        >
          <Link
            href="#"
            className="font-bold hover:underline underline-offset-4"
          >
            (주)그레타
          </Link>
          <div>
            <FooterLink href="#">서비스 이용약관</FooterLink> |{' '}
            <FooterLink href="#">개인정보 처리방침</FooterLink>
          </div>
        </div>
        <div className="text-left leading-5 text-muted-foreground">
          <p>
            서울시 서대문구 신촌로 141 은하빌딩 302호 | 대표번호 070-8648-1024 |
            고객문의 ***@***.***
          </p>
          <p>© GRETA Inc. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;

'use client';

import { useAtomValue } from 'jotai';

import {
  buildICHierarchy,
  DomainType,
  IndustryType,
} from '@/app/home/_lib/format-operations';
import { Button } from '@/components/ui/button';
import { showThemeAtom } from '@/lib/atoms/base';

import styles from './value-chain-map.module.css';

type DivisionColorType = { [key: string]: string };
const divisionColor: DivisionColorType = {
  '1': 'bg-[#2f2f2f]',
  '2': 'bg-[#4d4d73]',
  '3': 'bg-[#8d7200]',
  '4': 'bg-[#264d73]',
  '5': 'bg-[#76003b]',
  '6': 'bg-[#216321]',
};

const DomainCard = ({ domainItem }: { domainItem: DomainType }) => {
  const showTheme = useAtomValue(showThemeAtom);
  return (
    <div
      className={`flex flex-col gap-2 px-6 py-4 flex-auto box-border rounded-xl ${
        divisionColor[domainItem.domainDivision] || 'bg-primary'
      } ${styles[domainItem.domainCode]}`}
    >
      <div className="text-xs text-primary-foreground">
        {domainItem.domainName}
      </div>

      {domainItem.industryClassList.length > 0 && (
        <div className={styles.icContainer}>
          {domainItem.industryClassList.map((icItem, ci) => {
            let ictName = icItem.industryClassName;
            if (ictName.includes('유틸리티')) {
              ictName = ictName.replace('유틸리티', '\n유틸리티');
            } else if (ictName.includes('/')) {
              ictName = ictName.replace('/', '/\n');
            } else if (ictName.includes('(')) {
              ictName = ictName.replace('(', '\n(');
            }

            return (
              <Button
                key={ci}
                size={'sm'}
                variant={
                  icItem.industryClassType.toLowerCase() === 'c'
                    ? 'secondary'
                    : 'default'
                }
                className={`px-1 h-10 overflow-hidden whitespace-pre-line
              ${
                icItem.industryClassType.toLowerCase() === 't' &&
                !showTheme &&
                'hidden'
              }
              `}
              >
                {ictName}
              </Button>
            );
          })}
        </div>
      )}
    </div>
  );
};

const ValueChainMap = ({ data }: { data: IndustryType[] }) => {
  const icData = buildICHierarchy(data);
  console.log(icData);

  return (
    <section className="container">
      <div className={styles.container}>
        {icData.map((item, i) => (
          <DomainCard key={i} domainItem={item} />
        ))}
      </div>
    </section>
  );
};

export default ValueChainMap;

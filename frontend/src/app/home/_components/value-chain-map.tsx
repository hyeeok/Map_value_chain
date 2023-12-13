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
      className={`flex flex-col gap-2 px-6 py-4 flex-auto box-border rounded-md ${
        divisionColor[domainItem.domainDivision] || 'bg-primary'
      } ${styles[domainItem.domainCode]}`}
    >
      <div className="inline-block flex justify-between text-primary-foreground">
        {domainItem.domainName}
      </div>
      <div>
        {domainItem.classList.length > 0 ? (
          <div className="flex flex-wrap gap-2">
            {domainItem.classList.map((classItem, ci) => (
              <Button
                key={ci}
                size={'sm'}
                variant={'secondary'}
                className="h-10"
              >
                {classItem.industryClassName.split('/')[0]}
                {classItem.industryClassName.split('/')[1] ? (
                  <>
                    / <br /> {classItem.industryClassName.split('/')[1]}
                  </>
                ) : null}
              </Button>
            ))}
          </div>
        ) : null}
        {domainItem.themeList.length > 0 && showTheme ? (
          <div className="pt-2 flex flex-wrap gap-2">
            {domainItem.themeList.map((themeItem, ti) => (
              <Button key={ti} size={'sm'} className="h-10">
                {themeItem.industryClassName.split('/')[0]}
                {themeItem.industryClassName.split('/')[1] ? (
                  <>
                    / <br /> {themeItem.industryClassName.split('/')[1]}
                  </>
                ) : null}
              </Button>
            ))}
          </div>
        ) : null}
      </div>
    </div>
  );
};

const ValueChainMap = ({ data }: { data: IndustryType[] }) => {
  const icData = buildICHierarchy(data);
  console.log(icData);

  return (
    <div className={styles.container}>
      {icData.map((item, i) => (
        <DomainCard key={i} domainItem={item} />
      ))}
    </div>
  );
};

export default ValueChainMap;

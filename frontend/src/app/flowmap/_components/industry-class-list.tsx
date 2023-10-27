'use client';

import { useAtomValue } from 'jotai';
import React from 'react';

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { showThemeAtom } from '@/lib/atoms/base';

export interface IndustryClass {
  industryClassId: number;
  industryClassCode: string;
  industryClassName: string;
  domainId: number;
  domainName: string;
  domainCode: string;
}
export interface IndustryClassList {
  industryClassListData: {
    length: number;
    data: IndustryClass[];
  };
}

const IndustryClassList = ({ industryClassListData }: IndustryClassList) => {
  const showTheme = useAtomValue(showThemeAtom);

  return (
    <div>
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead className="w-[150px]">Domain</TableHead>
            <TableHead className="w-[120px]">Code</TableHead>
            <TableHead className="w-[220px]">Industry Class</TableHead>
            <TableHead></TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {industryClassListData.data
            .filter(
              (IndustryClassItem) =>
                showTheme || IndustryClassItem.industryClassCode[2] !== 'T'
            )
            .map((industryClassItem, i) => (
              <TableRow key={i}>
                <TableCell className="font-medium">
                  {industryClassItem.domainName}
                </TableCell>
                <TableCell>{industryClassItem.industryClassCode}</TableCell>
                <TableCell>{industryClassItem.industryClassName}</TableCell>
                <TableCell></TableCell>
              </TableRow>
            ))}
        </TableBody>
      </Table>
    </div>
  );
};

export default IndustryClassList;

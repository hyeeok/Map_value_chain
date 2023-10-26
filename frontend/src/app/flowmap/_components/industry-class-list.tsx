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
  id: number;
  code: string;
  name: string;
  type: string;
  domain_id: number;
  domain_name: string;
  domain_code: string;
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
              (IndustryClassItem) => showTheme || IndustryClassItem.type !== 'T'
            )
            .map((industryClassItem, i) => (
              <TableRow key={i}>
                <TableCell className="font-medium">
                  {industryClassItem.domain_name}
                </TableCell>
                <TableCell>{industryClassItem.code}</TableCell>
                <TableCell>{industryClassItem.name}</TableCell>
                <TableCell></TableCell>
              </TableRow>
            ))}
        </TableBody>
      </Table>
    </div>
  );
};

export default IndustryClassList;

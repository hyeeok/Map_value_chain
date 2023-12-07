'use client';

import { useSearchParams } from 'next/navigation';
import { useEffect, useState } from 'react';

import { getOverviewhList } from '@/api/overview/api';
import OverviewList from '@/app/overview/_components/overview-list';

const OverviewSearchPage = () => {
  const searchParams = useSearchParams();
  const params = {
    category: searchParams.get('category') || null,
    keyword: searchParams.get('keyword') || null,
    limit: searchParams.get('limit') || '20',
    page: searchParams.get('page') || '1',
  };
  const [overviewData, setOverviewData] = useState();

  useEffect(() => {
    getOverviewhList({
      category: params.category,
      keyword: params.keyword,
      limit: params.limit,
      page: params.page,
    })
      .then((response) => {
        console.log(response);
        setOverviewData(response);
      })
      .catch();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [searchParams]);
  return <div>{overviewData && <OverviewList data={overviewData} />}</div>;
};

export default OverviewSearchPage;

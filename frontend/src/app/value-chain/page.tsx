import { cookies } from 'next/headers';
import React from 'react';

import { baseUrl } from '@/api/api-client';
import ValueChain from '@/app/value-chain/_components/value-chain';

const getIndustryClassList = async () => {
  const cookieStore = cookies();
  try {
    const response = await fetch(`${baseUrl}/industry`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.log(error);
  }
};

const ValueChainPage = async () => {
  const industryData = await getIndustryClassList();

  return (
    <div className="min-h-[calc(100vh-45px)] flex flex-col">
      <section className="">
        {industryData ? (
          <ValueChain data={industryData} />
        ) : (
          <div>No data found.</div>
        )}
      </section>
    </div>
    // <div className="container py-4">
    //   <ValueChain data={industryData} />
    // </div>
  );
};

export default ValueChainPage;

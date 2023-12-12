import React from 'react';

import VCMap from '@/app/home/_components/vc-map';
import { IC_DATA } from '@/app/home/_test/industry-classes';

const icData = IC_DATA;

const HomePage = () => {
  return (
    <div className="container py-4">
      <VCMap data={icData} />
    </div>
  );
};

export default HomePage;

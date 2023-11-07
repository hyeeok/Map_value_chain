import React from 'react';

// import IndustryInfo from '@/app/search/_components/industry-info';
import SearchResult from '@/app/search/_components/search-result';

// 진입시 query 존재 여부 확인
// query 없는 경우 빈화면 표시
// query 있는 경우 get
// 검색 -> ?name=blah로 이동 -> page 표시 -> query에서 blah 추출 -> 데이터 표시

const SearchPage = () => {
  return (
    <div className="flex flex-col">
      <SearchResult />
      {/* <IndustryInfo /> */}
    </div>
  );
};

export default SearchPage;

import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchOption, setSearchOption] = useState('name');
  const [searchResults, setSearchResults] = useState([]);
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      if (searchTerm.trim() === '') {
        setSearchResults([]);
        return;
      }

      try {
        const response = await fetch(`http://localhost:8000/overview/search?term=${searchTerm}&option=${searchOption}`);
        const data = await response.json();
        setSearchResults(data.length > 0 ? data : []);
      } catch (error) {
        console.error('에러 발생:', error);
      }
    };

    fetchData();
  }, [searchTerm, searchOption]);

  const handleInputChange = (e) => {
    setSearchTerm(e.target.value);
  };

  const handleSelectChange = (e) => {
    setSearchOption(e.target.value);
  };

  const handleResultClick = (result) => {
    setSearchTerm(searchOption === 'name' ? result.name : result[searchOption]);
    setSearchResults([]);
  };

  const handleConfirmClick = async () => {
    try {
      if (searchTerm.trim() === '') {
        alert('검색어를 입력해주세요.');
        return;
      }

      const response = await fetch(`http://localhost:8000/overview?term=${searchTerm}&option=${searchOption}`);
      const resultData = await response.json();

      if (resultData.length > 0) {
        setData(resultData);
      } else {
        alert('데이터가 없습니다.');
      }

      // 검색 완료 후 입력값 초기화
      setSearchTerm('');
    } catch (error) {
      console.error('에러가 발생했습니다:', error);
      alert('에러가 발생했습니다.');
    }
  };

  return (
    <form>
      <div className="search-container">
        <select onChange={handleSelectChange} value={searchOption}>
          <option value="name">회사명</option>
          <option value="registration_number">사업자등록번호</option>
          <option value="corporate_type">법인등록번호</option>
          <option value="stock_code">증권종목코드</option>
        </select>
        <input type="text" value={searchTerm} onChange={handleInputChange} />
        {searchResults.length > 0 && (
          <div className="search-results">
            <ul>
              {searchResults.map((result) => (
                <li key={result.id} onClick={() => handleResultClick(result)}>
                  {searchOption === 'name' ? result.name : `${result[searchOption]} - ${result.name}`}
                </li>
              ))}
            </ul>
          </div>
        )}
        <button type="button" onClick={handleConfirmClick}>
          검색
        </button>
      </div>
      {data && data.length > 0 && (
        <div className="search-results table-container">
          <table>
            <thead>
              <tr>
                <th>회사명</th>
                <th>사업자등록번호</th>
                <th>법인등록번호</th>
                <th>증권종목코드</th>
                <th>자회사 여부</th>
                <th>대표이사</th>
                <th>설립일</th>
                <th>지역</th>
                <th>웹사이트</th>
              </tr>
            </thead>
            <tbody>
              {data.data.map((result) => (
                <tr key={result.name}>
                  <td>{result.name}</td>
                  <td>{result.registration_number}</td>
                  <td>{result.corporate_type}</td>
                  <td>{result.stock_code}</td>
                  <td>{result.subsidiary_mock ? '자회사' : '비자회사'}</td>
                  <td>{result.ceo_name}</td>
                  <td>{result.establishment_date}</td>
                  <td>{result.region}</td>
                  <td>
                    <a href={result.website}>
                      {result.website}
                    </a>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </form>
  );
}

export default App;

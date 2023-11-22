import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchCategory, setSearchCategory] = useState('firm');
  const [searchResults, setSearchResults] = useState([]);
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      if (searchTerm.trim() === '') {
        setSearchResults([]);
        return;
      }

      try {
        const response = await fetch(`http://localhost:8000/overview/search?term=${searchTerm}&category=${searchCategory}`);
        const data = await response.json();
        setSearchResults(data.length > 0 ? data : []);
      } catch (error) {
        console.error('에러 발생:', error);
      }
    };

    fetchData();
  }, [searchTerm, searchCategory]);

  const handleInputChange = (e) => {
    setSearchTerm(e.target.value);
  };

  const handleSelectChange = (e) => {
    setSearchCategory(e.target.value);
  };

  const handleResultClick = (result) => {
    setSearchTerm(searchCategory === 'firm' ? result.firm : result[searchCategory]);
    setSearchResults([]);
  };

  const handleConfirmClick = async () => {
    try {
      if (searchTerm.trim() === '') {
        alert('검색어를 입력해주세요.');
        return;
      }

      const response = await fetch(`http://localhost:8000/overview?term=${searchTerm}&category=${searchCategory}`);
      const resultData = await response.json();

      if (resultData.length > 0) {
        setData(resultData);
      } else {
        alert('데이터가 없습니다.');
      }
      setSearchTerm('');
    } catch (error) {
      console.error('에러가 발생했습니다:', error);
      alert('에러가 발생했습니다.');
    }
  };

    const handleSubmit = (e) => {
      e.preventDefault(); // 기본 폼 제출 동작 방지
      handleConfirmClick();
    };

  return (
    <form onSubmit={handleSubmit}>
      <div className="search-container">
        <select onChange={handleSelectChange} value={searchCategory}>
          <option value="firm">회사명</option>
          <option value="bizr_no">사업자등록번호</option>
          {/* <option value="corp_cls">법인등록번호</option> */}
          <option value="stock_code">종목코드</option>
        </select>
        <input type="text" value={searchTerm} onChange={handleInputChange} />
        {searchResults.length > 0 && (
          <div className="search-results">
            <ul>
              {searchResults.map((result) => (
                <li onClick={() => handleResultClick(result)}>
                  {searchCategory === 'firm' ? result.firm : `${result[searchCategory]} - ${result.firm}`}
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
                <th>설립일</th>
                <th>지역(대)</th>
                <th>지역(소)</th>
              </tr>
            </thead>
            <tbody>
              {data.data.map((result) => (
                <tr>
                  <td>{result.firm}</td>
                  <td>{result.bizr_no}</td>
                  <td>{result.corp_cls}</td>
                  <td>{result.stock_code}</td>
                  <td>{result.bsns_year}</td>
                  <td>{result.adres_1}</td>
                  <td>{result.adres_2}</td>
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

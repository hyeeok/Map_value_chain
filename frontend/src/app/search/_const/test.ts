export const SIDENAV = {
  domainTab: [
    {
      domainName: '도메인1',
      industryList: [
        { industryName: '산업1' },
        { industryName: '산업2' },
        { industryName: '산업3' },
      ],
    },
    {
      domainName: '도메인2',
      industryList: [{ industryName: '산업1' }, { industryName: '산업2' }],
    },
  ],
  industryTab: [
    {
      mainCategoryName: '대분류',
      middleCategoryList: [
        {
          middleCategoryName: '중분류',
          smallCategoryList: [
            { smallCategoryName: '소분류1' },
            { smallCategoryName: '소분류2' },
            { smallCategoryName: '소분류3' },
          ],
        },
        {
          middleCategoryName: '중분류',
          smallCategoryList: [
            { smallCategoryName: '소분류1' },
            { smallCategoryName: '소분류2' },
          ],
        },
      ],
    },
    {
      mainCategoryName: '대분류',
      middleCategoryList: [
        {
          middleCategoryName: '중분류',
          smallCategoryList: [{ smallCategoryName: '소분류1' }],
        },
      ],
    },
  ],
};

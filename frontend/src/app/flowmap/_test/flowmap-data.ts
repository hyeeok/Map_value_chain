const initialNodes = [
  {
    id: '1',
    position: { x: 0, y: 0 },
    data: {
      domainName: '농림축수산',
      color: 1,
      classes: [
        { industryClassName: '농축산업' },
        { industryClassName: '수산업' },
        { industryClassName: '임업' },
      ],
      themes: [{ industryClassName: '스마트팜' }],
    },
    type: 'custom',
  },
  {
    id: '2',
    position: { x: 200, y: 0 },
    data: {
      domainName: '의학/헬스케어',
      color: 2,
      classes: [
        { industryClassName: '반려동물/수의학' },
        { industryClassName: '바이오/생물공학' },
        { industryClassName: '제약/의약품' },
        { industryClassName: '의료기기/용품' },
        { industryClassName: '헬스케어 기술/서비스' },
        { industryClassName: '의료기관 및 서비스' },
      ],
      themes: [
        { industryClassName: '백신/방역/진단시약' },
        { industryClassName: '실버산업/시니어' },
        { industryClassName: '건강 기능식품' },
        { industryClassName: '메디컬뷰피/더마코스메틱' },
        { industryClassName: '원격진료' },
      ],
    },
    type: 'custom',
  },
];

const initialEdges = [
  {
    id: '1-2',
    source: '1',
    sourceHandle: 'right',
    target: '2',
    targetHandle: 'left',
  },
];

export { initialEdges, initialNodes };

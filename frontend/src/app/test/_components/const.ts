const nodes = [
  {
    id: '1',
    position: { x: 0, y: 0 },
    data: { label: '농림축수산' },
    type: 'custom',
  },
  {
    id: '2',
    position: { x: 200, y: 0 },
    data: { label: '의학/헬스케어' },
    type: 'custom',
  },
  {
    id: '3',
    position: { x: 0, y: 200 },
    data: { label: '금융/부동산' },
    type: 'custom',
  },
  {
    id: '4',
    position: { x: 200, y: 200 },
    data: { label: '에너지/자원' },
    type: 'custom',
  },
];

const edges = [
  {
    id: '1-2',
    source: '1',
    sourceHandle: 'right',
    target: '2',
    targetHandle: 'left',
  },
  {
    id: '1-4',
    source: '1',
    sourceHandle: 'bottom',
    target: '4',
    targetHandle: 'top',
  },
];

const mvc = [
  {
    category: '농림축수산',
    domains: [{ label: '농축산업' }],
    themes: [{ label: '스마트팜' }],
  },
  {
    category: '의학/헬스케어',
    domains: [
      { label: '반려동물/수의학' },
      { label: '바이오/생물공학' },
      { label: '제약/의약품' },
    ],
    themes: [{ label: '백신/방역/진단시약' }, { label: '실버산업/시니어' }],
  },
  {
    category: '금융/부동산',
    domains: [{ label: '은행' }],
    themes: [{ label: '인터넷/은행' }, { label: '핀테크/전자결제' }],
  },
  {
    category: '에너지/자원',
    domains: [{ label: '신재생 에너지' }],
    themes: [],
  },
];

export { edges, mvc, nodes };

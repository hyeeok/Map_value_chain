module.exports = {
  env: {
    browser: true,
    es2021: true
  },
  extends: ['standard-with-typescript', 'plugin:react/recommended'],
  overrides: [
    {
      env: {
        node: true
      },
      files: ['.eslintrc.{js,cjs}'],
      parserOptions: {
        sourceType: 'script'
      }
    }
  ],
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module'
  },
  plugins: ['react', 'simple-import-sort', 'import', 'unused-imports'],
  rules: {
    'react/prop-types': 'off',
    // js 사용시 missing in props validation 에러 제거
    'simple-import-sort/imports': 'error',
    // import문의 sort 규칙 설정
    'simple-import-sort/exports': 'error',
    // export문의 sort 규칙 설정
    'import/first': 'error',
    // 모든 import문이 파일 선두에 위치해 있는 것 확인
    'import/newline-after-import': 'error',
    // import문 아래 빈 줄 확인
    'import/no-duplicates': 'error',
    // 같은 파일의 import문 머지
    'unused-imports/no-unused-imports': 'error'
    // 미사용 import문 삭제
  }
}

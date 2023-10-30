import { Edge, Node } from 'reactflow';

import { apiClient } from '@/api/api-client';

// export const getFlowmap = async () => {
//   try {
//     const response = await apiClient().get(`/flowmap`);
//     return response.data;
//   } catch (error) {
//     throw error;
//   }
// };

// export const getFlowmap = async () => {
//   const cookieStore = cookies();
//   try {
//     const response = await fetch(`${baseUrl}/flowmap`);
//     const data = await response.json();
//     return data;
//   } catch (error) {
//     throw error;
//   }
// };

interface newData {
  node: Node[];
  edge: Edge[];
}
export const putFlowmap = async (newData: newData) => {
  try {
    const response = await apiClient().put(`/flowmap`, newData);
    return response.data;
  } catch (error) {
    throw error;
  }
};

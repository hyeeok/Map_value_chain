import { apiClient } from '@/api/api-client';

export const getFlowmap = async () => {
  try {
    const response = await apiClient().get(`/flowmap`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

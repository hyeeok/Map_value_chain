'use client';

import React from 'react';
import { Handle, Position } from 'reactflow';

import { mvc } from '@/app/test/_components/const';

import styles from './custom-node.module.css';

interface DataProps {
  data: { label: string };
}

const CustomNode = ({ data }: DataProps) => {
  const mvcObj = mvc.find((item) => item.category === data.label);
  console.log(mvcObj);

  return (
    <div>
      <Handle type="target" position={Position.Top} id="top" />
      <Handle type="target" position={Position.Right} id="right" />
      <Handle type="target" position={Position.Left} id="left" />
      <Handle type="target" position={Position.Bottom} id="bottom" />
      <label>{data.label}</label>
      <div className={styles.domain}>
        {mvcObj?.domains?.map((domain, i) => <div key={i}>{domain.label}</div>)}
      </div>
      <div className={styles.theme}>
        {mvcObj?.themes?.map((theme, i) => <div key={i}>{theme.label}</div>)}
      </div>
      <Handle type="source" position={Position.Top} id="top" />
      <Handle type="source" position={Position.Right} id="right" />
      <Handle type="source" position={Position.Left} id="left" />
      <Handle type="source" position={Position.Bottom} id="bottom" />
    </div>
  );
};

export default CustomNode;

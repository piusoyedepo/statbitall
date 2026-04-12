import { motion, useReducedMotion } from 'framer-motion';
import type { ReactNode } from 'react';

interface Props {
  children: ReactNode;
  /** Stagger delay in seconds */
  delay?: number;
}

export default function ScrollReveal({ children, delay = 0 }: Props) {
  const shouldReduce = useReducedMotion();

  // No wrapper at all when reduced motion is preferred
  if (shouldReduce) {
    return <>{children}</>;
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 16 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '-20px' }}
      transition={{ duration: 0.4, ease: 'easeOut', delay }}
      style={{ willChange: 'transform, opacity' }}
    >
      {children}
    </motion.div>
  );
}

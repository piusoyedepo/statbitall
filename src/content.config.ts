import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    module: z.enum(['A', 'B', 'C', 'D', 'E']),
    date: z.date(),
    readTime: z.string(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { blog };

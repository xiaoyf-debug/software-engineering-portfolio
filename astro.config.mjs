import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

// 使用 Tailwind CSS 官方 Vite 插件，不引入额外 UI 或动画依赖。
export default defineConfig({
  site: 'https://xiaoyf-debug.github.io',
  base: '/software-engineering-portfolio',
  vite: {
    plugins: [tailwindcss()],
  },
});

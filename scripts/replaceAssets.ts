import fs from 'node:fs';
import path from 'node:path';

const readDirRecursive = async (filePath: string): Promise<string[]> => {
  const dir = await fs.promises.readdir(filePath);
  const files = await Promise.all(
    dir.map(async (relativePath) => {
      const absolutePath = path.join(filePath, relativePath);
      const stat = await fs.promises.lstat(absolutePath);
      return stat.isDirectory() ? readDirRecursive(absolutePath) : absolutePath;
    })
  );
  return files.flat();
};

const files = await readDirRecursive('./dist-front');
if (files) {
  Array.from(files).forEach((file) => {
    if (
      !(
        file.endsWith('.js') ||
        file.endsWith('.html') ||
        file.endsWith('.map') ||
        file.endsWith('.css')
      )
    ) {
      return;
    }
    fs.readFile(file, 'utf8', (_, data) => {
      fs.writeFile(file, data.replace(/http:\/\/REPLACEME/g, '.'), 'utf8', () => {
        console.log("Wrote file '" + file + "'");
      });
    });
  });
}

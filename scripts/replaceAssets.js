import fs from 'fs';
import path from 'path';

const readDirRecursive = async (filePath) => {
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
  fs.readFile(file, 'utf8', (err, data) => {
    fs.writeFile(file, data.replace(/http:\/\/REPLACEME/g, '.'), 'utf8', () => {
      console.log("Wrote file '" + file + "'");
    });
  });
});

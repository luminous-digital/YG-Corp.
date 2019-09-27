let gulp = require('gulp');
let styleguide = require('sc5-styleguide');
let sass = require('gulp-sass');
let concat = require('gulp-concat');

let sourcePath = 'src';
let staticPath = 'static';
let styleSourcePath = sourcePath + '/scss';
let scssWild = styleSourcePath + '/**/*.scss';
let scssRoot = styleSourcePath + '/main.scss';
let extraScssRoot = styleSourcePath + '/styleguide.scss';

let styleguideTmpPath = 'styleguide';
let isProdOrCommit = global.production || !!~process.argv.indexOf('commit');

gulp.task('sgimages', function() {
  gulp
    .src(staticPath + '/img/**.*')
    .pipe(gulp.dest(styleguideTmpPath + '/static/img'));
});

gulp.task('sgsvg', function() {
  gulp
    .src(staticPath + '/svg/symbol/svg/sprite.symbol.svg')
    .pipe(gulp.dest(styleguideTmpPath + '/static/svg/symbol/svg'));
});

gulp.task('sgjs', function() {
  gulp
    .src(staticPath + '/js/**.*')
    .pipe(gulp.dest(styleguideTmpPath + '/static/js'));
});

gulp.task('sgfonts', function() {
  gulp
    .src(staticPath + '/fonts/**.*')
    .pipe(gulp.dest(styleguideTmpPath + '/static/fonts'));
});

gulp.task('styleguide:generate', function() {
  return gulp
    .src(scssWild)
    .pipe(
      styleguide.generate({
        title: 'YouGov Styleguide',
        extraHead: ['<script src="/static/js/app.js"></script>'],
        disableEncapsulation: true,
        server: !isProdOrCommit,
        rootPath: styleguideTmpPath,
        overviewPath: 'README.md',
        showReferenceNumbers: true,
        appRoot: isProdOrCommit ? '/styleguide' : '',
      })
    )
    .pipe(gulp.dest(styleguideTmpPath));
});

gulp.task('styleguide:applystyles', function() {
  return gulp
    .src([scssRoot, extraScssRoot])
    .pipe(concat('all.scss'))
    .pipe(
      sass({
        errLogToConsole: true,
      })
    )
    .pipe(styleguide.applyStyles())
    .pipe(gulp.dest(styleguideTmpPath));
});

gulp.task('styleguidewatch', ['styleguide'], function() {
  // Start watching changes and update styleguide whenever changes are detected
  // Styleguide automatically detects existing server instance
  gulp.watch([scssWild], ['styleguide']);
});

gulp.task('styleguide', [
  'styleguide:generate',
  'styleguide:applystyles',
  'sgimages',
  'sgsvg',
  'sgjs',
  'sgfonts',
]);

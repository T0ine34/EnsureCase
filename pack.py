from feanor import BaseBuilder


class Builder(BaseBuilder):
    def Setup(self):
        self.addDirectory('src', 'ensure-case')
        self.addAndReplaceByPackageVersion('pyproject.toml')

    # def Tests(self):
    #     self.addDirectory('tests')
    #     self.addFile('requirements.txt')
    #     self.addFile('melkor.config.json')
    #     self.venv().InstallFromRequirements('requirements.txt')
    #     self.venv().install('feanorTempDir')
    #     self.venv().runMelkor('melkor.config.json')

    def Build(self):
        self.venv().install('build')
        self.venv().runModule(f'build --outdir {self.distDir} .')

from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "tea_engine.cy.vector",
        ["src/tea_engine/cy/vector.pyx"],
    ),
    Extension(
        "tea_engine.cy.renderer_concat",
        ["src/tea_engine/cy/renderer_concat.pyx"],
    ),
    Extension(
        "tea_engine.cy.spacegrid",
        ["src/tea_engine/cy/spacegrid.pyx"],
    ),
]

setup(
    name="tea_engine",
    package_dir={"": "src"},
    packages=[
        "tea_engine",
        "tea_engine.cy",
    ],
    ext_modules=cythonize(
        ext_modules,
        compiler_directives={"language_level": "3"},
    ),
)

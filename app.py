from flask import Flask, render_template, url_for, request, flash, redirect
from colorizers.siggraph17 import siggraph17
from server import colorize

app = Flask(__name__)

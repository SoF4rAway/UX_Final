from flask import Blueprint, render_template

views=Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/profile')
def profile():
    return render_template('profile.html')

@views.route('/academic')
def academic():
    judul = 'Kalender Akademik'
    ref_link = 'https://drive.google.com/file/d/1y0IEjJWMLb-JVc7guaiI8Pq0EO7HWqvq/preview'
    down_link = 'https://drive.google.com/uc?export=download&id=1y0IEjJWMLb-JVc7guaiI8Pq0EO7HWqvq'
    return render_template('academic.html', judul=judul, ref_link=ref_link, down_link=down_link)

@views.route('/academic-dtk')
def academicdtk():
    judul = 'Kurikulum Dept. Teknik Komputer'
    ref_link = 'https://drive.google.com/file/d/1y0IEjJWMLb-JVc7guaiI8Pq0EO7HWqvq/preview'
    down_link = 'https://drive.google.com/uc?export=download&id=1y0IEjJWMLb-JVc7guaiI8Pq0EO7HWqvq'
    return render_template('academic.html', judul=judul, ref_link=ref_link, down_link=down_link)

@views.route('/academic-dsi')
def academicdsi():
    judul = 'Kurikulum Dept. Sistem Informasi'
    ref_link = 'https://drive.google.com/file/d/1y0IEjJWMLb-JVc7guaiI8Pq0EO7HWqvq/preview'
    down_link = 'https://drive.google.com/uc?export=download&id=1y0IEjJWMLb-JVc7guaiI8Pq0EO7HWqvq'
    return render_template('academic.html', judul=judul, ref_link=ref_link, down_link=down_link)

@views.route('/academic-dif')
def academicdif():
    judul = 'Kurikulum Dept. Informatika'
    ref_link = 'https://drive.google.com/file/d/1y0IEjJWMLb-JVc7guaiI8Pq0EO7HWqvq/preview'
    down_link = 'https://drive.google.com/uc?export=download&id=1y0IEjJWMLb-JVc7guaiI8Pq0EO7HWqvq'
    return render_template('academic.html', judul=judul, ref_link=ref_link, down_link=down_link)

@views.route('/links')
def links():
    return render_template('links.html')

@views.route('/documents')
def documents():
    return render_template('documents.html')

@views.route('/data-alumni')
def database():
    return render_template('database.html')

@views.route('/publication')
def publication():
    return render_template('publication.html')

@views.route('/gallery')
def gallery():
    return render_template('gallery.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')
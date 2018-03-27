from flask import render_template, request

from app import app, get_conn


def get_pages():
    conn = get_conn()
    papers = conn.get_nums
    if papers and papers >= 10:
        page = papers // 10
        return page + 1
    return 1

@app.route('/')
@app.route('/index')
def new_paper():
    """
    拿到最新壁纸
    """
    conn = get_conn()
    paper = conn.get_new()
    return render_template('paper.html', paper=paper, title='今日壁纸')


@app.route('/papers')
def all_papers():
    page = request.args.get('page', 1, type=int)
    pages = get_pages()

    next = True if pages > page else False
    prev = False if page == 1 else True
    conn = get_conn()
    papers = conn.get_page(page, 10)[0]

    return render_template('papers.html', papers=papers, pages=pages,
                           page=page, next=next, prev=prev)


@app.route('/paper/<int:num>')
def paper(num):
    conn = get_conn()
    paper = conn.get_data(num)
    return render_template('paper.html', paper=paper)

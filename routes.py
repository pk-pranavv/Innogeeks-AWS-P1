from flask import Flask, render_template, request
import aws_bucket

app=Flask(__name__)



@app.route('/')
def fun():
    return render_template('index.html')

@app.route('/createbucket')
def add():
    return render_template('add.html',var='createbucket')



@app.route('/createbucket/success', methods=['POST'])
def function1():
    if request.method=='POST':
        bucket_name=request.form['name']
        location=request.form['Location']
    return aws_bucket.createbucket(bucket_name, location)


@app.route('/listallbuckets')
def function2():
    return aws_bucket.listallbuckets()


@app.route('/getbucketpolicy')
def add1():
    return render_template('add.html',var='getbucketpolicy')

@app.route('/getbucketpolicy/success',methods=['POST'])
def function3():
    if request.method=='POST':
        bucket_name=request.form['name']
    return aws_bucket.getbucketpolicy(bucket_name)


@app.route('/creationtime')
def function4():
    return aws_bucket.creationTime()

@app.route('/deletebucketpolicy')
def add2():
    return render_template('add.html',var='deletebucketpolicy')


@app.route('/deletebucketpolicy/success',methods=['POST'])
def function5():
    if request.method=='POST':
        bucket_name=request.form['name']
    return aws_bucket.deletebucketpolicy(bucket_name)



@app.route('/uploadfile')
def function6():
    return aws_bucket.uploadfile()


@app.route('/downloadfile')
def function6():
    return aws_bucket.downloadfile()


if __name__=='__main__':
    app.run(debug=True)
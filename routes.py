from flask import Flask, render_template, request, redirect
import aws_bucket, aws_ec2
import os

app=Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "pkkkkkkk1213"


@app.route('/')
def fun():
    return render_template('home.html')


@app.route('/EC2')
def EC2():
    return render_template('Ec2.html')

@app.route('/S3')
def home():
    return render_template('index.html')

@app.route('/createbucket')
def add():
    return render_template('add.html',var='createbucket')



# Routing For AWS Buckets Starts Here...

@app.route('/createbucket/success', methods=['POST'])
def function1():
    if request.method=='POST':
        bucket_name=request.form['name']
        location=request.form['Location']
    return aws_bucket.createbucket(bucket_name, location)


@app.route('/listallbuckets')
def function2():
    mybucket = []
    mybucket = aws_bucket.listallbuckets()
    return render_template('new.html', mybucket=mybucket)


@app.route('/getbucketpolicy')
def add1():
    return render_template('add.html',var='getbucketpolicy')

@app.route('/getbucketpolicy/success',methods=['POST'])
def function3():
    if request.method=='POST':
        bucket_name=request.form['name']
    return aws_bucket.getbucketpolicy(bucket_name)

@app.route('/listfiles')
def add3():
    return render_template('add.html',var='listfiles')

@app.route('/listfiles/success',methods=['POST'])
def function4():
    if request.method=='POST':
        bucket_name=request.form['name']
    return aws_bucket.listfiles(bucket_name)


@app.route('/deletebucketpolicy')
def add2():
    return render_template('add.html',var='deletebucketpolicy')

@app.route('/deletebucketpolicy/success',methods=['POST'])
def function5():
    if request.method=='POST':
        bucket_name=request.form['name']
    return aws_bucket.deletebucketpolicy(bucket_name)



@app.route('/uploadfile')
def functionupload():
    return render_template('add.html',var='upload')

@app.route('/uploadfile/success', methods=['POST'])
def function6():
    if request.method=='POST':
        bucket_name=request.form['name']
    f = request.files['file']
    f.save(os.path.join(UPLOAD_FOLDER, f.filename))
    return aws_bucket.uploadfile(f"uploads/{f.filename}", bucket_name)


@app.route('/downloadfile')
def function7():
    return aws_bucket.downloadfile()




# Routing For EC2 Instances Starts Here...

@app.route('/createinstance')
def function_A():
    return render_template('add1.html',var="create")

@app.route('/createinstance/success', methods=['POST'])
def function_B():
    keyname=request.form['name']
    return aws_ec2.create_instance(keyname)



@app.route('/getrunninginstances')
def function_C():
    newlist = [[]]
    newlist = aws_ec2.get_running_instances()
    return render_template('new.html', newlist = newlist, var = 'getinstance')

@app.route('/stopinstance')
def function_D():
    return render_template('add1.html',var='stopinstance')

@app.route('/stopinstance/success', methods=['POST'])
def function_E():
    name=request.form['name']
    return aws_ec2.stopinstance(name)

@app.route('/getpublicip')
def function_F():
    return render_template('add1.html',var='getpublicip')

@app.route('/getpublicip/success',methods=['POST'])
def function_G():
    name=request.form['name']
    return aws_ec2.get_public_ip(name)

@app.route('/terminateinstance')
def function_H():
    return render_template('add1.html',var='terminate')

@app.route('/terminateinstance/success',methods=['POST'])
def function_I():
    name=request.form['name']
    return aws_ec2.terminateinstance(name)

@app.route('/rebootinstance')
def function_J():
    return render_template('add1.html',var='reboot')

@app.route('/reboot/success',methods=['POST'])
def function_K():
    name=request.form['name']
    return aws_ec2.rebootinstance(name)

@app.route('/describeinstance')
def function_L():
    return render_template('add1.html',var='describe')



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)